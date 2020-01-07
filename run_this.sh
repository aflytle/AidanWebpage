rm -r lib64
rm -r lib
rm -r lib64
rm -r bin
rm -r include
echo "removed venv... reinstalling..."
python3 -m venv . && echo "done!!" || echo "Failed for some reason"
source bin/activate 
echo "reinstalling dependencies"
pip install -r requirements.txt && echo "DONE" || echo "This failed ᕙ(⇀‸↼‶)ᕗ"

