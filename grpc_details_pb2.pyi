from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class addNumbersReq(_message.Message):
    __slots__ = ("num1", "num2")
    NUM1_FIELD_NUMBER: _ClassVar[int]
    NUM2_FIELD_NUMBER: _ClassVar[int]
    num1: int
    num2: int
    def __init__(self, num1: _Optional[int] = ..., num2: _Optional[int] = ...) -> None: ...

class rawImageReq(_message.Message):
    __slots__ = ("img",)
    IMG_FIELD_NUMBER: _ClassVar[int]
    img: bytes
    def __init__(self, img: _Optional[bytes] = ...) -> None: ...

class rawJsonReq(_message.Message):
    __slots__ = ("imgString",)
    IMGSTRING_FIELD_NUMBER: _ClassVar[int]
    imgString: str
    def __init__(self, imgString: _Optional[str] = ...) -> None: ...

class dotProductReq(_message.Message):
    __slots__ = ("num1", "num2")
    NUM1_FIELD_NUMBER: _ClassVar[int]
    NUM2_FIELD_NUMBER: _ClassVar[int]
    num1: _containers.RepeatedScalarFieldContainer[float]
    num2: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, num1: _Optional[_Iterable[float]] = ..., num2: _Optional[_Iterable[float]] = ...) -> None: ...

class addition(_message.Message):
    __slots__ = ("sum",)
    SUM_FIELD_NUMBER: _ClassVar[int]
    sum: int
    def __init__(self, sum: _Optional[int] = ...) -> None: ...

class dotProduct(_message.Message):
    __slots__ = ("dotProduct",)
    DOTPRODUCT_FIELD_NUMBER: _ClassVar[int]
    dotProduct: float
    def __init__(self, dotProduct: _Optional[float] = ...) -> None: ...

class rawImageDims(_message.Message):
    __slots__ = ("width", "height")
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class jsonImageDims(_message.Message):
    __slots__ = ("width", "height")
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
