<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Automation Scripts Collection</title>
</head>
<body>

<h1>🖥️ Automation Scripts Collection</h1>

<p>This repository contains 3 small Python utilities that automate different tasks:</p>

<hr>

<h2>1️⃣ <code>auto_git_push.py</code> - Automatic Git Commit and Push</h2>

<h3>Description:</h3>
<ul>
  <li>Continuously monitors a directory (<strong>githarkat</strong>) for file changes.</li>
  <li>After detecting 50 file changes, it automatically:
    <ul>
      <li>Stages all changes</li>
      <li>Commits with message: <code>Automatic commit</code></li>
      <li>Pushes to GitHub</li>
    </ul>
  </li>
</ul>

<h3>Requirements:</h3>
<ul>
  <li>Install dependencies:</li>
</ul>

<pre><code>pip install gitpython watchdog
</code></pre>

<ul>
  <li>Make sure your repo path inside the script is correctly set:</li>
</ul>

<pre><code>repo_path = '/home/himanshu1009/Desktop/everything_in_here/GITDEMO/githarkat'
</code></pre>

<ul>
  <li>Make sure Git credentials are configured for your repo.</li>
</ul>

<h3>Run:</h3>

<pre><code>python3 auto_git_push.py
</code></pre>

<hr>

<h2>2️⃣ <code>cleanup.py</code> - Cleanup Unwanted Files</h2>

<h3>Description:</h3>
<ul>
  <li>Compares files inside two folders:</li>
  <ul>
    <li><code>~/Desktop/Temporary/Himanshu</code></li>
    <li><code>~/Desktop/Temporary/TripImages</code></li>
  </ul>
  <li>Deletes files from TripImages which do not exist (by filename) inside Himanshu.</li>
</ul>

<h3>Use case:</h3>
<p>Keep only filtered trip images based on a reference folder.</p>

<h3>Run:</h3>

<pre><code>python3 cleanup.py
</code></pre>

<p>⚠️ <strong>Caution:</strong> Files will be permanently deleted. Double check before running.</p>

<hr>

<h2>3️⃣ <code>share_images.py</code> - Google Drive Share Automation</h2>

<h3>Description:</h3>
<ul>
  <li>Uses Google Drive API to automatically share a file/folder with multiple email addresses.</li>
</ul>

<h3>Requirements:</h3>
<ul>
  <li>Google Service Account JSON key file.</li>
  <li>Enable Google Drive API on Google Cloud Console.</li>
  <li>Update:</li>
</ul>

<pre><code>SERVICE_ACCOUNT_FILE = '/path/to/service_account_key.json'
</code></pre>

<ul>
  <li>Install dependencies:</li>
</ul>

<pre><code>pip install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2
</code></pre>

<h3>Run:</h3>

<pre><code>python3 share_images.py
</code></pre>

<hr>

<h2>🔧 Global Setup Instructions</h2>
<ul>
  <li>Python 3.x</li>
  <li>Use virtual environment (recommended):</li>
</ul>

<pre><code>python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
</code></pre>

<h3>Create <code>requirements.txt</code> file with:</h3>

<pre><code>gitpython
watchdog
google-api-python-client
google-auth
google-auth-oauthlib
google-auth-httplib2
</code></pre>

<hr>

<h2>✅ Optional: Git Preparation before push</h2>

<ul>
  <li>You can create a simple <code>.gitignore</code> file to ignore:</li>
</ul>

<pre><code>*.pyc
__pycache__/
service_account_key.json
</code></pre>

<p><strong>Note:</strong> Never push your <code>service_account_key.json</code> file to GitHub.</p>

</body>
</html>
