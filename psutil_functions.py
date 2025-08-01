import psutil

class SystemMeasure:

    def __init__(self):
        self.outputObject = {}


    def measureCPU(self):
        self.outputObject['CPUPercentageUsage'] = psutil.cpu_percent(interval=1)
    def measureMemory(self):
        memory = psutil.virtual_memory()
        self.outputObject['RAMUsagePercentage'] = memory.percent
        self.outputObject['TotalRamInGigaBytes'] = memory.total/1000000000
        self.outputObject['AvailableRAM'] = memory.available/1000000000

    def getTopProcesses(self, limit):
        processes = []
        
        for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
            try:
                processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        processes = [p for p in processes if p['memory_percent'] is not None]
        processes.sort(key=lambda x: x['memory_percent'], reverse=True)

        self.outputObject['topProcesses'] = processes[:limit]


    def returnAll(self):
        self.measureCPU()
        self.measureMemory()
        self.getTopProcesses(5)

        return self.outputObject

