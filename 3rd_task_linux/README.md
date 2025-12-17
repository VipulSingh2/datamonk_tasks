# Task 3 — File Permissions & Security


✅ Answer 1 — Understanding Execute Permission 🔑

For files, execute permission means you can actually run the file like a script or program.
For directories, execute permission means you’re allowed to enter or access the directory.

Even if you have read permission, you still can’t view what’s inside the directory unless you also have execute permission.
It’s basically like having a list of rooms but not being allowed to walk into them 🚪🙂

✅ Answer 2 — Why 777 Permissions Are Dangerous 🔥

Setting a file or folder to 777 means everyone gets full access — read, write, and execute.

On a web server this is a big risk.
If a script has 777, then anyone could upload files, change things, or run malicious code. That can make your whole site vulnerable ⚠️

So it’s always better to give only the permissions that are needed, nothing extra 👍

✅ Answer 3 — The Power (and Risk) of sudo ⚡

The sudo command basically gives you root access, meaning you can do almost anything on the system.

This is useful, but also risky because one wrong command can break things or change important system files 😅
So it's important to use sudo only when necessary and be sure about what the command does.

