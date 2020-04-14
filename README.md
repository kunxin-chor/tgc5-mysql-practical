# Installing PhpMyAdmin with GitPod

Demonstrate how to use PhpMyAdmin with a project created from the code institute Gitpod Template.

The commands are found in `install-phpmyadmin.sh` - the file is now automatically run as part of the `init_tasks.sh` script inside the `.theia` folder. If you are interested in just install PHPMyAdmin for an existing GitPod instance, you can just copy the script over in a .sh file (and be sure to set the executable permission with `chmod -u=rwx` on the file first!).

You still need to do one manual step to configure PHPMyAdmin correctly:

To setup PHPMyAdmin for GitPod:

1. Find the file `public/phpmyadmin/config.inc.php`
2. Look for the string `AllowNoPassword`
3. Change the line to read: `$cfg['Servers'][$i]['AllowNoPassword'] = true;` and *remember to save*
4. Start apache with `apachectl start` and when the pop-up appears, click `Open Browser`
5. At the browser, add `/phpmyadmin` to the end of the URL in the address bar
6. Login with user `root` and no password.

