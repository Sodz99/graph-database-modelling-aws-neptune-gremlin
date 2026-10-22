# To uncompress files to different directories:
for i in `ls *.zip`; do unzip $i -d ./"${i%%.*}"/; done

# To copy uncompressed files, back to S3:
aws s3 cp ./1035264248_T_ONTIME_MARKETING_Jan_2018/1035264248_T_ONTIME_MARKETING.csv s3://us-bts-raw-euwest1-14317621-dev/flights-performance-raw-csv/year=2018/month=01/
aws s3 cp ./1035264248_T_ONTIME_MARKETING_Feb_2018/1035264248_T_ONTIME_MARKETING.csv s3://us-bts-raw-euwest1-14317621-dev/flights-performance-raw-csv/year=2018/month=02/
aws s3 cp ./1035264248_T_ONTIME_MARKETING_Mar_2018/1035264248_T_ONTIME_MARKETING.csv s3://us-bts-raw-euwest1-14317621-dev/flights-performance-raw-csv/year=2018/month=03/
aws s3 cp ./1035264248_T_ONTIME_MARKETING_Jan_2021/1035264248_T_ONTIME_MARKETING.csv s3://us-bts-raw-euwest1-14317621-dev/flights-performance-raw-csv/year=2021/month=01/
aws s3 cp ./1035264248_T_ONTIME_MARKETING_Feb_2021/1035264248_T_ONTIME_MARKETING.csv s3://us-bts-raw-euwest1-14317621-dev/flights-performance-raw-csv/year=2021/month=02/
aws s3 cp ./1035264248_T_ONTIME_MARKETING_Mar_2021/1035264248_T_ONTIME_MARKETING.csv s3://us-bts-raw-euwest1-14317621-dev/flights-performance-raw-csv/year=2021/month=03/