HELP_DATA = [
    {
        "category": "Target Configuration",
        "items": [
            {
                "cmd": "-u, --url",
                "title": "Target URL",
                "desc": "The main target to scan. Specify the full URL including protocol and vulnerable parameter.",
                "example": "http://example.com/page.php?id=1",
            },
            {
                "cmd": "-g",
                "title": "Google Dork",
                "desc": "Use a Google dork expression as an alternative target. sqlmap fetches results via Google Search and tests each one.",
                "example": "inurl:admin.php?id=",
            },
            {
                "cmd": "--method",
                "title": "HTTP Method",
                "desc": "Force the HTTP method for requests. Default is GET unless --data is provided (POST is auto-selected).",
            },
            {
                "cmd": "--data",
                "title": "POST Data",
                "desc": "Data string to send in the HTTP body (for POST, PUT, etc.). Can be a query string, JSON, or XML.",
                "example": "id=1&name=test",
            },
            {
                "cmd": "-p",
                "title": "Testable Parameter(s)",
                "desc": "Specify which parameter(s) to test. By default sqlmap tests all provided parameters.",
                "example": "id,name,search",
            },
            {
                "cmd": "--skip",
                "title": "Skip Parameter(s)",
                "desc": "Skip testing certain parameter(s). Useful when parameters cause side effects (logout, CSRF tokens).",
                "example": "token,csrf",
            },
            {
                "cmd": "--prefix",
                "title": "Injection Prefix",
                "desc": "Add a custom prefix to every injection payload. Used when the vulnerable parameter is inside a custom SQL query structure.",
                "example": "')",
            },
            {
                "cmd": "--suffix",
                "title": "Injection Suffix",
                "desc": "Add a custom suffix to every injection payload. Used together with --prefix.",
                "example": "--",
            },
        ],
    },
    {
        "category": "HTTP Request Configuration",
        "items": [
            {
                "cmd": "--cookie",
                "title": "HTTP Cookie",
                "desc": "Set a cookie value for the HTTP request. Required when the target requires cookie-based authentication.",
            },
            {
                "cmd": "--user-agent",
                "title": "Custom User-Agent",
                "desc": "Set a custom User-Agent header. If left empty, --random-agent is used automatically.",
            },
            {
                "cmd": "--referer",
                "title": "HTTP Referer",
                "desc": "Set a custom Referer header. Some applications validate the Referer header.",
            },
            {
                "cmd": "--host",
                "title": "HTTP Host",
                "desc": "Set a custom Host header. Useful for virtual-host routing or Host header validation.",
            },
            {
                "cmd": "--headers",
                "title": "Custom Headers",
                "desc": "Add custom HTTP headers. One header per line, format: Header-Name: value.",
            },
            {
                "cmd": "--auth-type",
                "title": "Auth Type",
                "desc": "HTTP authentication type. Supported: Basic, Digest, NTLM, Bearer (token).",
            },
            {
                "cmd": "--auth-cred",
                "title": "Auth Credentials",
                "desc": "Credentials in format username:password for Basic/Digest/NTLM authentication.",
                "example": "admin:password123",
            },
            {
                "cmd": "--auth-file",
                "title": "Auth File",
                "desc": "A PEM certificate file for client-side certificate authentication (e.g., mutual TLS).",
            },
            {
                "cmd": "--proxy",
                "title": "HTTP Proxy",
                "desc": "Use an HTTP/HTTPS/SOCKS proxy for all requests.",
                "example": "http://127.0.0.1:8080",
            },
            {
                "cmd": "--proxy-file",
                "title": "Proxy File",
                "desc": "Load a list of proxies from a file. sqlmap rotates through them.",
            },
            {
                "cmd": "--tor",
                "title": "Tor Network",
                "desc": "Route all requests through the Tor network (requires Tor on localhost:9050).",
            },
            {
                "cmd": "--check-tor",
                "title": "Verify Tor",
                "desc": "Verify Tor connection is working before starting the scan.",
            },
            {
                "cmd": "--delay",
                "title": "Request Delay",
                "desc": "Set a delay (seconds) between each HTTP request to avoid rate limiting.",
            },
            {
                "cmd": "--timeout",
                "title": "Request Timeout",
                "desc": "Maximum time (seconds) to wait for an HTTP response. Default: 30.",
            },
            {
                "cmd": "--retries",
                "title": "Retry Count",
                "desc": "Number of times to retry a failed HTTP request. Default: 3.",
            },
        ],
    },
    {
        "category": "Injection Configuration",
        "items": [
            {
                "cmd": "--dbms",
                "title": "Database Management System",
                "desc": "Force the back-end DBMS type. Useful when sqlmap has trouble auto-detecting. Supports 22 database types (MySQL, Oracle, PostgreSQL, etc.).",
            },
            {
                "cmd": "--level",
                "title": "Test Level (1-5)",
                "desc": "Comprehensiveness of tests. 1=Default basic tests, 2-3=adds Cookie/User-Agent header tests, 4-5=tests more parameters and heavy payloads. Higher levels are significantly slower.",
            },
            {
                "cmd": "--risk",
                "title": "Risk Level (1-3)",
                "desc": "Risk of causing damage. 1=Safe (no dangerous payloads), 2=Medium (more aggressive), 3=Dangerous (OR-based, heavy time-based). Risk 3 may modify data or cause DoS.",
            },
            {
                "cmd": "--threads",
                "title": "Threads",
                "desc": "Number of parallel threads for faster scans. Max recommended: 10. Higher = faster but less stealthy.",
            },
            {
                "cmd": "--technique",
                "title": "SQL Injection Techniques",
                "desc": "Select which injection techniques to use. By default all are enabled. B=Boolean-based, E=Error-based, U=UNION query, S=Stacked queries, T=Time-based blind, Q=Inline queries.",
            },
            {
                "cmd": "--tamper",
                "title": "Tamper Scripts",
                "desc": "WAF/IDS evasion scripts that modify payloads to bypass filters. Select multiple as needed. Examples: space2comment, base64encode, between.",
            },
            {
                "cmd": "--os",
                "title": "Target OS",
                "desc": "Force the back-end operating system (Linux/Windows) for OS-specific payloads.",
            },
            {
                "cmd": "--invalid-bignum",
                "title": "Invalid Big Number",
                "desc": "Use a custom big number to replace invalid values during detection.",
                "example": "999999",
            },
            {
                "cmd": "--no-cast",
                "title": "No CAST",
                "desc": "Disable the CAST() function during data extraction. May help with certain DBMS versions.",
            },
            {
                "cmd": "--no-escape",
                "title": "No Escape",
                "desc": "Disable string escaping in payloads. Useful when the DBMS uses non-standard escaping.",
            },
            {
                "cmd": "--hex",
                "title": "Hex Conversion",
                "desc": "Use hexadecimal representation for data extraction. Helps bypass certain filtering mechanisms.",
            },
        ],
    },
    {
        "category": "Enumeration & Data Extraction",
        "items": [
            {
                "cmd": "--all",
                "title": "Retrieve Everything",
                "desc": "Retrieve everything accessible: all databases, tables, columns, and data entries.",
            },
            {
                "cmd": "--banner",
                "title": "DBMS Banner",
                "desc": "Retrieve the DBMS banner (version, patch level, additional details).",
            },
            {
                "cmd": "--current-user",
                "title": "Current User",
                "desc": "Retrieve the current database user name.",
            },
            {
                "cmd": "--current-db",
                "title": "Current Database",
                "desc": "Retrieve the current database name.",
            },
            {
                "cmd": "--is-dba",
                "title": "Is DBA?",
                "desc": "Check if the current user has DBA (database administrator) privileges.",
            },
            {
                "cmd": "--hostname",
                "title": "DBMS Hostname",
                "desc": "Retrieve the DBMS hostname.",
            },
            {
                "cmd": "--users",
                "title": "Enumerate Users",
                "desc": "Enumerate all DBMS users.",
            },
            {
                "cmd": "--passwords",
                "title": "Enumerate Passwords",
                "desc": "Enumerate and crack password hashes for all DBMS users.",
            },
            {
                "cmd": "--privileges",
                "title": "User Privileges",
                "desc": "Retrieve privilege information for each user.",
            },
            {
                "cmd": "--roles",
                "title": "User Roles",
                "desc": "Retrieve roles assigned to each user.",
            },
            {
                "cmd": "--dbs",
                "title": "List Databases",
                "desc": "List all databases on the server.",
            },
            {
                "cmd": "--tables",
                "title": "Enumerate Tables",
                "desc": "Enumerate tables in a specific database. Use with -D.",
            },
            {
                "cmd": "--columns",
                "title": "Enumerate Columns",
                "desc": "Enumerate columns in a specific table. Use with -D and -T.",
            },
            {
                "cmd": "--schema",
                "title": "Full Schema",
                "desc": "Retrieve the full DBMS schema (all databases, tables, columns).",
            },
            {
                "cmd": "-D",
                "title": "Database Name",
                "desc": "Specify a database to target for enumeration (e.g., with --tables or --dump).",
                "example": "database_name",
            },
            {
                "cmd": "-T",
                "title": "Table Name",
                "desc": "Specify a table to target (e.g., with --columns or --dump).",
                "example": "users",
            },
            {
                "cmd": "-C",
                "title": "Column Names",
                "desc": "Specify specific columns to enumerate or dump (comma-separated).",
                "example": "id,username,password",
            },
            {
                "cmd": "--dump",
                "title": "Dump Table Data",
                "desc": "Dump data from a specific table. Use -D, -T, -C to target precisely.",
            },
            {
                "cmd": "--dump-all",
                "title": "Dump All Data",
                "desc": "Dump all data from all tables in all databases.",
            },
            {
                "cmd": "--search",
                "title": "Search Data",
                "desc": "Search for specific data (columns, tables, or databases matching a pattern).",
            },
            {
                "cmd": "--start / --stop",
                "title": "Row Range",
                "desc": "Limit dump output to a range of rows. Useful for large tables with millions of rows.",
            },
            {
                "cmd": "--csv-del",
                "title": "CSV Delimiter",
                "desc": "Set CSV delimiter character (default: comma). Used with CSV output format.",
            },
            {
                "cmd": "--json",
                "title": "JSON Output",
                "desc": "Format output data as JSON for programmatic processing.",
            },
            {
                "cmd": "--xml",
                "title": "XML Output",
                "desc": "Format output data as XML.",
            },
        ],
    },
    {
        "category": "Operating System Access",
        "items": [
            {
                "cmd": "--os-shell",
                "title": "Interactive OS Shell",
                "desc": "Request an interactive OS shell on the target DB server. Requires DBA privileges.",
            },
            {
                "cmd": "--os-pwn",
                "title": "OOB Shell / Meterpreter",
                "desc": "Attempt OOB (out-of-band) shell, Meterpreter, or VNC session. More advanced than --os-shell.",
            },
            {
                "cmd": "--read-file",
                "title": "Read File",
                "desc": "Read a file from the target DBMS file system. Requires DBA privileges and DB functions (e.g., LOAD_FILE in MySQL).",
                "example": "/etc/passwd",
            },
            {
                "cmd": "--write-file",
                "title": "Write File",
                "desc": "Write a local file to the target DBMS file system. Typically used to upload a web shell.",
                "example": "/var/www/html/shell.php",
            },
            {
                "cmd": "--dest",
                "title": "Destination Path",
                "desc": "Target destination path for --write-file (if different from the source path).",
                "example": "C:\\inetpub\\wwwroot\\shell.php",
            },
            {
                "cmd": "--reg-read",
                "title": "Registry Read",
                "desc": "Read a Windows registry key value. Requires DBA on Windows targets.",
            },
            {
                "cmd": "--reg-add",
                "title": "Registry Add",
                "desc": "Add or modify a Windows registry key value.",
            },
            {
                "cmd": "--reg-del",
                "title": "Registry Delete",
                "desc": "Delete a Windows registry key value.",
            },
            {
                "cmd": "--reg-key",
                "title": "Registry Key Path",
                "desc": "Specify the registry key path for registry operations.",
                "example": "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\...",
            },
            {
                "cmd": "--reg-value",
                "title": "Registry Value Name",
                "desc": "Specify the registry value name to read, add, or delete.",
            },
            {
                "cmd": "--reg-data",
                "title": "Registry Data",
                "desc": "Specify the registry data to write (used with --reg-add).",
            },
            {
                "cmd": "--reg-type",
                "title": "Registry Value Type",
                "desc": "Registry value type: REG_SZ (string), REG_DWORD (32-bit int), REG_BINARY (binary).",
            },
        ],
    },
    {
        "category": "General Options",
        "items": [
            {
                "cmd": "--batch",
                "title": "Batch Mode",
                "desc": "Run in non-interactive mode. sqlmap uses default answers for all prompts. Recommended for automated scanning.",
            },
            {
                "cmd": "--flush-session",
                "title": "Flush Session",
                "desc": "Delete the session file for the current target and re-scan from scratch.",
            },
            {
                "cmd": "--fresh-queries",
                "title": "Fresh Queries",
                "desc": "Ignore cached queries in the session file. Re-run all queries against the target.",
            },
            {
                "cmd": "--session-file",
                "title": "Session File",
                "desc": "Use a custom session file path instead of ~/.sqlmap/. Lets you manage multiple independent scans.",
            },
            {
                "cmd": "-v",
                "title": "Verbosity Level (0-6)",
                "desc": "Control output verbosity: 0=Silent, 1=Default (info+warnings), 2-3=Detailed (headers), 4-5=Debug (full traffic), 6=Trace (internal debug).",
            },
            {
                "cmd": "--output-dir",
                "title": "Output Directory",
                "desc": "Custom output directory for scan results. Default: ~/.sqlmap/output/.",
            },
            {
                "cmd": "--save",
                "title": "Save Config",
                "desc": "Save the current scan configuration to a session file for later reuse.",
            },
            {
                "cmd": "--keep-alive",
                "title": "Keep-Alive",
                "desc": "Use persistent HTTP connections (Connection: keep-alive). Faster but more detectable.",
            },
            {
                "cmd": "--null-connection",
                "title": "Null Connection",
                "desc": "Use HTTP null-connection (HEAD-like) for page comparison. Faster but less reliable.",
            },
            {
                "cmd": "--text-only",
                "title": "Text Only",
                "desc": "Compare text content only, ignoring HTML/JS/CSS. Useful when dynamic content varies.",
            },
            {
                "cmd": "--titles",
                "title": "Compare Titles",
                "desc": "Compare page titles (<title>) instead of full page content. Faster detection.",
            },
            {
                "cmd": "--string",
                "title": "Custom TRUE String",
                "desc": "Use a custom string that indicates a TRUE response (present when injection is valid).",
                "example": "Welcome",
            },
            {
                "cmd": "--not-string",
                "title": "Custom FALSE String",
                "desc": "Use a custom string that indicates a FALSE response (present when injection is invalid).",
                "example": "Error",
            },
            {
                "cmd": "--code",
                "title": "HTTP Status Code",
                "desc": "Match a specific HTTP status code (e.g., 200) to identify TRUE responses.",
            },
        ],
    },
]
