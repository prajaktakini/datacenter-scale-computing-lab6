import io
from base64 import b64decode
from concurrent import futures
import grpc
from PIL import Image
import grpc_details_pb2
import grpc_details_pb2_grpc

class GrpcServer(grpc_details_pb2_grpc.lab6serviceStub):
    def __init__(self):
        pass

    def doAdd(self, request, context):
        try:
            print(f"Add num 1 {request.num1}, num 2 {request.num2}")
            return grpc_details_pb2.addition(sum = request.num1 + request.num2)
        except Exception as e:
            print(e)

    def doRawImage(self, request, context):
        try:
            print("Dimensions of raw image ")
            image = Image.open(io.BytesIO(request.img))
            return grpc_details_pb2.rawImageDims(width=image.width, height=image.height)
        except Exception as e:
            print(e)

    def doDotProduct(self, request, context):
        try:
            print(f"Do dot product of num 1 {request.num1}, num 2 {request.num2}")
            prod = 0.0
            for num1, num2 in zip(request.num1, request.num2):
                prod += num1 * num2
            return grpc_details_pb2.dotProduct(dotProduct=prod)
        except Exception as e:
            print(e)

    def doJsonImage(self, request, context):
        try:
            print("Dimensions of json image ")
            image = Image.open(io.BytesIO(b64decode(request.imgString)))
            return grpc_details_pb2.jsonImageDims(width=image.width, height=image.height)
        except Exception as e:
            print(e)

def serve():
    print("Initialising GRPC server")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_details_pb2_grpc.add_lab6serviceServicer_to_server(GrpcServer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

serve()