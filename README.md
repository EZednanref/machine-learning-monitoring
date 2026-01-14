# machine-learning-monitoring

Projet final de cours de microservices.

## Structure du projet

```
machine-learning-monitoring/
├── backend/
│   ├── app/ <- Service backend principal
│   │   ├── main.py
    │   ├── auth.py
    │   ├── security.py
    │   └── database.py
    ├── requirements.txt
│   └── Dockerfile
├── trainer/ <- Service du training des modèles
│   ├── train.py
│   ├── metrics.py
│   └── Dockerfile
├── kafka/
│   └── docker-compose.kafka.yml
├── database/
│   ├── init.sql
│   └── Dockerfile
├── frontend/
│   ├── Dockerfile
│   └── src/
└── docker-compose.yml
```

## gif du sinje

![](gif.gif)
