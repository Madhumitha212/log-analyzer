from faker import Faker
import random

fake = Faker()
log_level = ["ERROR","ALERT", "SUCCESS","WARNING"]
http_code = [200, 201, 300, 301, 302, 400, 401, 403, 404, 500]

def generate_data():
        """Generate fake log entry"""
        date_time = fake.date_time()
        ip_address = fake.ipv4()
        log_level1 = random.choice(log_level)
        description = fake.sentence(nb_words = 4)
        status = random.choice(http_code)
        return "{} {} {} {} {}\n".format(date_time, log_level1 , description, ip_address, status)

def write_in_file(filename,num_records):
    """Write multiple log entries to a file.""" 
    with open(filename, "w") as file: 
         for _ in range(num_records): 
              record = generate_data() 
              file.write(record)
    
def main():
    write_in_file("server_log.txt", 20)

if __name__ == "__main__":
     main()
