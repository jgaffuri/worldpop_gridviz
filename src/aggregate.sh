
for year in "2000" "2010" "2020"; do
    for res in "2" "5" "10" "20" "50" "100" "200" "500"; do
        echo "$year" "$res"
        gdalwarp -tr $res $res -r sum -tap "/home/juju/geodata/worldpop/ppp_"$year"_1km_Aggregated.tif" /home/juju/geodata/worldpop/ppp_"$year"_"$res"km_Aggregated.tif
    done
done

