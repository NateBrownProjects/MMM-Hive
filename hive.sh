cd ~/Desktop/MagicMirror/
npm run
DISPLAY=1
cd ..
source TheHiveProject/bin/activate || source TheHiveProject/Scripts/activate
cd MMM-Hive/ || cd MMM-Hive
git pull
python hive.py
