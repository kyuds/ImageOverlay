number="$1"

if [ ! -d "result" ]; then
    mkdir result
fi

if [ ! $number ]; then
    python generate.py
else
    python generate.py --n $number
fi
