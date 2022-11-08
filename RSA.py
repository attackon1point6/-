import rsa
import base64

with open('public.txt', 'rb') as f:
    pubkey = f.read()
with open('private.txt', 'rb') as f:
    privkey = f.read()

pubkey = rsa.PublicKey.load_pkcs1(pubkey)
privkey = rsa.PrivateKey.load_pkcs1(privkey)

def rsaEncrypt(content, pubkey):
    '''
    对字符串进行公钥加密
    :param content: 被加密的字符串
    :return: 加密后的内容
    '''
    # content = content.encode('utf-8')#明文编码格式

    result = rsa.encrypt(content.encode(), pubkey)
    return result

def rsaDecrypt(result, privkey):
    '''
    利用rsa包进行私钥解密
    :param result: 被加密的内容
    :param privkey: 私钥
    :return: 解密后的内容
    '''
    result = base64.b64decode(result)
    print(result)
    content = rsa.decrypt(result, privkey).decode()
    # content = content.decode('utf-8')

    return content

if __name__ == '__main__':
    ############ 使用公钥 - 私钥对信息进行"加密" + "解密" ##############
    message = 'test'

    #利用rsa包生成公钥、私钥，
    # (pubkey, privkey) = rsa.newkeys(512)

    print(pubkey, privkey)
    # print(pubkey.save_pkcs1())
    # filename = 'public.pem'
    # pub = pubkey.save_pkcs1()
    # with open('public.pem','wb+')as f:
    #     f.write(pub)
    #
    # pri = privkey.save_pkcs1()
    # with open('private.pem','wb+')as f:
    #     f.write(pri)

    result = rsaEncrypt(message, pubkey)
    result = base64.b64encode(result)
    print('加密后的密文为：{}'.format(result))

    content = rsaDecrypt(result, privkey)
    print('解密后的明文为：{}'.format(content))
