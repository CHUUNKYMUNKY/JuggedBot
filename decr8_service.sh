DATE=`date '+%Y-%m-%d %H:%M:%S'`
echo "decr8 service started at ${DATE}" | systemd-cat -p info

while :
do
echo "Starting decr8 bot...";
python3 /home/ayuko/decr8/decr8_bot.py;
done
