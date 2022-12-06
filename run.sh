number="$1"
fail="$2"

if [ ! -d "result" ]; then
    mkdir result
fi

if [[ ! $number ]] && [[ ! $fail ]]; then
    python generate.py
elif [[ ! $fail ]]; then
    python generate.py --n $number
elif [[ ! $number ]]; then
    python generate.py --f $fail
fi
