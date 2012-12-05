from paver.setuputils import setup

setup(
    name = "pkgdemo",
    packages = ["pkgdemo"],
    version = "1.0",
    author = "Austin Marshall",
    package_data =
        {
            "pkgdemo": [
                "assets/*.txt", 
                "assets/css/*.css",
                "assets/js/*.js"
            ]
        },
    zip_safe=False,
    entry_points = 
        {
            "console_scripts": [
                "pkgdemo = pkgdemo.actions:main",
                "pkgdemo-foo = pkgdemo.actions:foo"
            ]
        }
)
