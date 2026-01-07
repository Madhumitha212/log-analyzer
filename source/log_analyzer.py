import re
import os
from collections import Counter

datetime_pattern = re.compile(r"\d{4}[\-:/]\d{2}[:\-?]\d{2} \d{2}:\d{2}:\d{2}") 
loglevel_pattern = re.compile(r"ERROR|ALERT|SUCCESS|WARNING") 
ip_pattern = re.compile(r"\d{1,3}\.\d{1,}\.\d{1,}\.\d{1,}") 
status_pattern = re.compile(r"\b(200|201|300|301|302|400|401|403|404)\b") 

def analyze_logs(filename):
    ips = set()
    status_count = {}

    with open(filename, "r") as infile: 
        """Analayse a log file to extract unique ip adress and 
        count the http codes"""
        for line in infile: 
            datetime = datetime_pattern.search(line)
            loglevel = loglevel_pattern.search(line) 
            ip = ip_pattern.search(line) 
            status = status_pattern.search(line) 
            if datetime and loglevel and ip and status:
                datetime = datetime.group()
                loglevel = loglevel.group()
                ip = ip.group()
                status = status.group() 

                ips.add(ip)

                if status not in status_count:
                    status_count[status] = 1
                else:
                    status_count[status] += 1
    return ips, status_count
def write_summary(filename, ips, status_count):
    """Extracted information is written into another file as 
    a summary"""
    with open(filename ,"w") as f:
        f.write("LOG SUMMARY:\n")

        f.write("--Unique IPs--\n")
        for ip in ips:
            f.write(f"{ip}\n")

        f.write("\n--status count--\n")
        f.write("code : count\n")
        for code, count in status_count.items():
            f.write(f"{code} : {count}\n")

def main():
    base_dir = os.path.dirname(__file__) 
    log_path = os.path.join(base_dir, "server_log.txt") 
    summary_path = os.path.join(base_dir, "log_summary.txt")

    ips, count = analyze_logs(log_path) 
    write_summary(summary_path, ips, count)
    # ips, count = analyze_logs("server_log.txt")
    # write_summary("log_summary.txt",ips, count)

if __name__ == "__main__":
    main()
    