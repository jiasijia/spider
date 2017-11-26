##python编码
1.python的字符串以str表示，python3的字符串在内存中以unicode编码表示
2.unicode编码的字节是固定的，一般是两个字节，因为英文只占用一个字节，所以如果都用unicode编码存储或传输数据的话，那么纯英文的文本会占用多一倍的空间，所以有了utf-8编码
3.utf-8编码是可变字节长度的编码，中文字符使用3个字节，英文字符使用一个字节
4.ascii是utf-8的子集，所以可以用ascii编码的字符也可以用utf-8编码
5.所以如果要在网络上传输就要把内存中的unicode编码的字节变成ascii或者utf-8编码的字节，比如‘abc'.encode('ascii') 或者'中文'.encode('utf-8')
6.解码 b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'),如果字节中包含无法解码的字节，就会报错，如果只有少部分无效字节，可以传入参数 errors="ignore"
7. decode的作用是将其他编码的字符串转换成unicode编码, encode的作用是将unicode编码转换成其他编码的字符串