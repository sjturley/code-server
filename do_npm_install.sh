for D in */; do
    if [ -d "${D}" ]; then
        echo "${D}"
        cd ${D}
        for D2 in */; do
            if [ -d "${D2}" ]; then
                echo "${D2}"
                cd ${D2}
                npm install
                cd ..
            fi
        done
        cd ..
    fi
done
