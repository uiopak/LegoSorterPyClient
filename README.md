### Dev
#### Generate proto files
`python -m grpc_tools.protoc -I ./proto --python_out=./generated --grpc_python_out=./generated ./proto/*.proto`