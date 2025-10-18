
test = './log1.txt'

def parse_log_line(file):
    
    with open(file, 'r', encoding='utf8') as f:
        logs = f.readlines()
        
        for log in logs:
            log_elements = log.split(' - ')
            print(log_elements.len())
            print(f'timestamp: {log_elements[0]} ')
            print(f'log_level: {log_elements[1]} ')
            print(f'module: {log_elements[2].split(":")[1]}')
            print(f'message: {log_elements[3]} ')
    
parse_log_line(test)
