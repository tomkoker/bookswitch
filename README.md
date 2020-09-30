<img src="server/static/assets/logo.png" alt="Logo" height="100">

# bookflip

[![Dependency Status](https://david-dm.org/tomkoker/bookflip.svg)](https://david-dm.org/tomkoker/bookflip)
[![Code Climate](https://codeclimate.com/github/tomkoker/bookflip/badges/gpa.svg)](https://codeclimate.com/github/tomkoker/bookflip)
[![Build Status](https://travis-ci.org/tomkoker/bookflip.svg?branch=master)](https://travis-ci.org/tomkoker/bookflip)

## Author
[Tom Koker](http://tomkoker.com)

## Installing

### Dependencies
**Virtual Env**:
```bash
sudo apt-get install python-pip
sudo pip install virtualenv
```

**Node**:
```bash
sudo apt-get install nodejs
sudo ln -s /usr/bin/nodejs /usr/bin/node
```

**Webpack**:
```bash
sudo npm install -g webpack
```

### The Installation
Clone and change directory:
```bash
git clone https://github.com/tomkoker/bookflip && cd bookflip
```

Create python virtual environment:
```bash
virtualenv -p /usr/bin/python2.7 venv
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
npm install
```

Create instance folder and config file:
```bash
mkdir instance && touch instance/config.py
```

Initialize database:
```bash
python init_db.py
```

Build and start the server:
```bash
webpack
python run.py
```

## Private API Documentation

**Responses**
All responses will look like the following:
```json
{
    "status": "success", // 'error' or 'fail'
    "data": {...}
}
```

**Routes**

| Location                                 | Input                     | Description           |
| ---------------------------------------- | ------------------------- | --------------------- |
| `/api/signup`                            | username, password, email | Creates a new user    |
| `/api/activate/<payload>`                |                           | Activates user        |
| `/api/login/`                            | username, password        | Logs in user          |
| `/api/logout/`                           |                           | Logs out user         |
| `/api/me/`                               |                           | Returns user status   |
| `POST: /api/listings/` | listing                   | Creates a new listing |
| `GET: /api/listings/` |                           | Shows all listings    |
|                                          |                           |                       |
|                                          |                           |                       |
|                                          |                           |                       |


## License

[AGPL-3.0](https://github.com/tomkoker/bookflip/blob/master/LICENSE)
