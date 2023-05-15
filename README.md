### Run
#### Reues LegoServerSorter env
`conda activate lego`
#### or create minimal new
`conda env create --file environment.yml`
`conda activate LegoSorterPyClient`

First run `camera-test.py` to check working parameters

Then edit `main.py` with corect parameters

### Dev
#### Generate proto files
`python -m grpc_tools.protoc -I ./proto --python_out=./generated --grpc_python_out=./generated ./proto/*.proto`