# Automated Penetration Testing Tool

This tool automates various penetration testing tasks, such as scanning, exploitation, and reporting.

## How to Use

1. Clone the repository.
2. Install the required dependencies.
3. Run the `pen_testing_tool.py` script.
4. Input the target IP address or range, exploit, and payload.

## Example

```python
Enter the target IP address or range: 192.168.1.1/24
Scanning network...
{scan results}
Enter the exploit to use: exploit/windows/smb/ms17_010_eternalblue
Enter the payload to use: windows/meterpreter/reverse_tcp
Exploiting target...
{exploit results}
Generating report...
{report}
