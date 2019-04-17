Title: Simple script for login to the FUM hotspot.
Date: 2019-04-17 17:43
Category: blog
Tags: Gnu/Linux; Bash; FUM
Slug: Simple-script-for-login-to-the-FUM-hotspot
Lang: en
Authors: Mohammad
Summary: Script for login to the FUM hotspot

If you want to simply login to the [FUM](http://um.ac.ir/) hotspot, do the followings:

At first you must compute the MD5 hash of your password:

```bash
echo -n "Password" | md5sum | awk '{print $1}'
```

Please replace the Password with yours.

Then create a simple bash script:

```bash
#!/bin/bash
while true; do
    curl --data "username=Username&password=HashedPass" https://hotspot.um.ac.ir/login > /dev/null
    sleep 100
done
```

You should replase the Username with your FUM one and the HashedPass with the output of the above command.

You can make this script executable and put it in your binary PATHs (for example ~/bin) for easier life.

To logout simply create another script like below:

```bash
#!/bin/bash
curl --data "username=Username&password=HashedPass" https://hotspot.um.ac.ir/logout > /dev/null
done
```
