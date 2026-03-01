# Dev Assessment - Webhook Receiver

Please use this repository for constructing the Flask webhook receiver.

*******************

## Setup

* Create a new virtual environment

```bash
pip install virtualenv
```

* Create the virtual env

```bash
virtualenv venv
```

* Activate the virtual env

```bash
source venv/bin/activate
```

* Install requirements

```bash
pip install -r requirements.txt
```

* Run the flask application (In production, please use Gunicorn)

```bash
python run.py
```

* The endpoint is at:

```bash
POST http://127.0.0.1:5000/webhook/receiver
```

You need to use this as the base and setup the flask app. Integrate this with MongoDB (commented at `app/extensions.py`)

*******************

Here is the section in **clean Markdown format**, ready to paste into your `README.md`:

---

```markdown
## MongoDB Setup (Atlas)

This project stores GitHub webhook events in MongoDB.

Follow the steps below to configure MongoDB:

---

### 1️⃣ Create MongoDB Atlas Account

- Go to: https://www.mongodb.com/cloud/atlas  
- Create a free account  
- Create a **Free (M0) cluster**

---

### 2️⃣ Create Database User

Inside Atlas:

- Go to **Database Access**
- Click **Add New Database User**
- Choose:
  - Username: `admin`
  - Password: (create strong password)
  - Role: **Read and Write to any database**
- Click **Create User**

---

### 3️⃣ Allow Network Access

Go to:

**Network Access → Add IP Address**

Click:

```

Allow Access From Anywhere (0.0.0.0/0)

```

---

### 4️⃣ Get Connection String

Go to:

**Clusters → Connect → Connect your application**

Copy the connection string.

It will look like:

```

mongodb+srv://admin:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority

```

Replace `<password>` with your database password and add database name `github`:

```

mongodb+srv://admin:YOUR_PASSWORD@cluster0.xxxxx.mongodb.net/github?retryWrites=true&w=majority

```

---

### 5️⃣ Configure Environment Variable

Create a `.env` file in the project root:

```

MONGO_URI=mongodb+srv://admin:YOUR_PASSWORD@cluster0.xxxxx.mongodb.net/github?retryWrites=true&w=majority

````

---

### 6️⃣ Install Required Packages

If not already installed:

```bash
pip install pymongo python-dotenv
````

---

### 7️⃣ Restart Flask Application

```bash
python run.py
```

Webhook events received at:

```
POST /webhook/receiver
```

will now be stored in:

```
Database: github
Collection: events
```

---

## Stored Event Schema

The application stores only minimal required fields:

```json
{
  "type": "push | pull_request | merge",
  "author": "username",
  "from_branch": "branch_name (if applicable)",
  "to_branch": "branch_name",
  "timestamp": "UTC datetime"
}
