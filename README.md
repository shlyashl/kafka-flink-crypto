# kafka-flink-crypto

### Проверить топики в кафке
```
docker exec -it kafka kafka-topics.sh \
  --list \
  --bootstrap-server kafka:9092
```

### Проверть наличие данных в топике 
```
docker exec -it kafka kafka-console-consumer.sh \
  --topic binance-data \
  --bootstrap-server kafka:9092 \
  --from-beginning
```