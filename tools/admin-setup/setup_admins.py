import os
import hashlib
import sys

def locate_app_js():
    possible_paths = [
        os.path.join(os.path.dirname(__file__), "..", "..", "app.js"),
        os.path.join(os.getcwd(), "app.js"),
        os.path.join(os.getcwd(), "tools", "admin-setup", "app.js"),
        os.path.join(os.getcwd(), "..", "..", "app.js")
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return os.path.abspath(path)
    return None

def main():
    print("=========================================")
    print("          GroupChat Admin Setup Tool     ")
    print("=========================================")
    
    app_js_path = locate_app_js()
    if not app_js_path:
        print("Error: Could not locate app.js file.")
        print("Please run this script from the project root or the tools/admin-setup/ directory.")
        sys.exit(1)
        
    print(f"Found app.js at: {app_js_path}")
    print("This tool will replace all current administrators with your new choices.")
    print("Let's add your new administrators.\n")
    
    admins = []
    while True:
        username = input("Enter admin username: ").strip().lower()
        if not username:
            print("Username cannot be empty.")
            continue
            
        password = input(f"Enter password for '{username}': ").strip()
        if not password:
            print("Password cannot be empty.")
            continue
            
        pwd_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        admins.append((username, pwd_hash))
        
        more = input("Do you want to add another admin? (y/n): ").strip().lower()
        if more != 'y':
            break
            
    js_roles = "\nconst ROLES = {\n"
    for username, pwd_hash in admins:
        js_roles += f"  '{username}': {{ passwordHash: '{pwd_hash}', role: 'admin', badge: null, label: 'Admin' }},\n"
    js_roles += "};\n\n"
    
    js_helper = (
        "// SHA-256 Hashing helper (Web Crypto API)\n"
        "async function sha256(message) {\n"
        "  const msgBuffer = new TextEncoder().encode(message);\n"
        "  const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);\n"
        "  const hashArray = Array.from(new Uint8Array(hashBuffer));\n"
        "  return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');\n"
        "}\n\n"
    )
    
    replacement_content = js_roles + js_helper
    
    with open(app_js_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_marker = "// ---- Roles & Passwords (SHA-256 Hashed) ----"
    end_marker = "// ---- Quick Reactions ----"
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx == -1 or end_idx == -1:
        print("Error: Could not locate configuration markers in app.js.")
        print("Ensure app.js has not been modified manually around the ROLES declaration.")
        sys.exit(1)
        
    before = content[:start_idx + len(start_marker)]
    after = content[end_idx:]
    
    new_content = before + "\n" + replacement_content + after
    
    with open(app_js_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("\nSuccess! Administrators have been updated in app.js.")
    print("New admins registered:")
    for username, _ in admins:
        print(f" - {username}")
    print("\nYou can now deploy or test your application.")

if __name__ == '__main__':
    main()
