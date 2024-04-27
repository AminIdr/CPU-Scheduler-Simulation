class Process:
    """
    Represents a process with attributes such as process ID, arrival time, burst time, and priority (if applicable).
    """

    def __init__(self, pid, arrival_time, burst_time, priority=None):
        """
        Initializes a new Process object.

        Args:
            pid (int): Process ID.
            arrival_time (int): Arrival time of the process.
            burst_time (int): Required CPU time (burst time) for the process.
            priority (int, optional): Priority of the process. Defaults to None.
        """
        self._pid = pid
        self._arrival_time = arrival_time
        self._burst_time = burst_time
        self._priority = priority
        self._completion_time = None

    @property
    def pid(self):
        """int: Process ID."""
        return self._pid

    @pid.setter
    def pid(self, value):
        """
        Sets the process ID.

        Args:
            value (int): Process ID to set.
        """
        self._pid = value

    @property
    def arrival_time(self):
        """int: Arrival time of the process."""
        return self._arrival_time

    @arrival_time.setter
    def arrival_time(self, value):
        """
        Sets the arrival time of the process.

        Args:
            value (int): Arrival time to set.
        """
        self._arrival_time = value

    @property
    def burst_time(self):
        """int: Required CPU time (burst time) for the process."""
        return self._burst_time

    @burst_time.setter
    def burst_time(self, value):
        """
        Sets the burst time of the process.

        Args:
            value (int): Burst time to set.
        """
        self._burst_time = value

    @property
    def priority(self):
        """int: Priority of the process."""
        return self._priority

    @priority.setter
    def priority(self, value):
        """
        Sets the priority of the process.

        Args:
            value (int): Priority to set.
        """
        self._priority = value

    @property
    def completion_time(self):
        """int: Completion time of the process."""
        return self._completion_time

    @completion_time.setter
    def completion_time(self, value):
        """
        Sets the completion time of the process.

        Args:
            value (int): Completion time to set.
        """
        self._completion_time = value

    def __str__(self):
        """
        Returns a string representation of the process.

        Returns:
            str: String representation of the process.
        """
        return f"Process {self._pid}: Arrival Time={self._arrival_time}, Burst Time={self._burst_time}, Priority={self._priority}, Completion Time={self._completion_time}"

    def __repr__(self):
        """
        Returns a string representation of the process (used for debugging).

        Returns:
            str: String representation of the process.
        """
        return self.__str__()
