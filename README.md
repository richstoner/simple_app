### Simple Application Example

Rich Stoner, 2014

##### Install

To be used with: https://github.com/richstoner/simple-application-framework

`fab last addApp:appname=simple,giturl=https://github.com/richstoner/simple_app.git`

`fab last enableApp:simple`

You can now start this app via the supervisor configuration

##### To update the app from git after enabled:

`fab last updateApp:simple`

`fab last restartAll` (this could be more elegant!)
