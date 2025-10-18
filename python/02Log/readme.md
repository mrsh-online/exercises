Here’s a practical Python exercise for a **log line parser**:

---

### Exercise: Log Line Parser

**Objective:**
Write a Python function called `parse_log_line` that takes a single log line (as a string) and returns a dictionary with the following parsed fields:

- `timestamp`: The date and time of the log entry (as a string)
- `log_level`: The severity level (e.g., "INFO", "ERROR", "WARNING")
- `message`: The actual log message
- `module`: The module or source of the log (if present)

**Example Log Line:**
```
2025-10-17 14:30:45,123 - ERROR - module:database - Connection timeout after 5 retries
```

**Expected Output:**
```python
{
    "timestamp": "2025-10-17 14:30:45,123",
    "log_level": "ERROR",
    "message": "Connection timeout after 5 retries",
    "module": "database"
}
```

**Requirements:**
- Handle log lines with and without the `module` field.
- Assume the log line format is consistent as in the example.
- Use string manipulation or regular expressions to parse the fields.

**Bonus:**
- Add error handling for malformed log lines.
- Write a function to parse multiple log lines from a file.

---
