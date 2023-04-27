Prepare embedded dataset using embedbase

run
`createDataset("docs/lettuce_hydroponic.yaml", "secrets.ini")`

`secret.ini`
```
[OPENAI]
OPENAI_API_KEY= <>
[EMBEDBASE]
EMBEDBASE_URL= <>
EMBEDBASE_KEY= <>
```

`{dataset_name}.yaml`
```yaml
'content':
- data: The level of ...
  metadata: {'size': 30, 'type': 'ambient'}
- data: Make sure your ...
  metadata: {'size': 15, 'type': 'light'}
    ...
```