cat $INPUT | awk '{
        if (substr($0, 1, 1)==">") {filename=(substr($0,2) ".fa")}
        print $0 > filename
}'
