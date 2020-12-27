import subprocess
import time
import logging
import os
import psutil


class Command:

    def __init__(self, cmd, log_file=None):

        self._cmd = cmd
        self._log_file = log_file
        self._start = time.time()

        start_log = f">>> Start command '{self._cmd}' <<<"
        logging.debug(start_log)
        if not self._log_file:
            self._proc = subprocess.Popen(self._cmd,
                                        shell=True,
                                        executable='/bin/csh',
                                        universal_newlines=True)
        else:
            assert os.path.exists(os.path.dirname(log_file))
            with open(self._log_file, 'a') as f:
                f.write(start_log + '\n')
                self._proc = subprocess.Popen(self._cmd,
                                            shell=True,
                                            executable='/bin/csh',
                                            universal_newlines=True,
                                            stdout=f,
                                            stderr=f)

    def communicate(self, timeout_s=None):
        elapsed = None
        try:
            self._proc.communicate(None, timeout_s)
        except subprocess.TimeoutExpired as e:
            self.kill()
            log = f">>> End command '{self._cmd}' with timeout error: {e.__str__()} <<<"
            logging.error(log)
        else:
            elapsed = time.time() - self._start
            log = ">>> End command '{}' in {:.3f} seconds <<<".format(self._cmd, elapsed)
            logging.debug(log)
        if self._log_file:
            with open(self._log_file, 'a') as f:
                f.write(log + '\n\n')
        return elapsed

    def kill(self):
        process = psutil.Process(self._proc.pid)
        kill_logs = []
        for child in process.children(recursive=True):
            kill_log = f">>> Kill command '{self._cmd}' child process '{child.pid}' - '{child.name()}' <<<"
            kill_logs.append(kill_log)
            logging.debug(kill_log)
            child.kill()

        kill_log = f">>> Kill command '{self._cmd}' process '{process.pid}' - '{process.name()}' <<<"
        kill_logs.append(kill_log)
        logging.debug(kill_log)
        process.kill()

        if self._log_file:
            with open(self._log_file, 'a') as f:
                for log in kill_logs:
                    f.write(log + '\n')

