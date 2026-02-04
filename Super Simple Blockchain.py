import time
import json
import hashlib

class Block: # 스스로 불러온 재앙에 짓눌려
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()
        
    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()  

  
class Blockchain:
    pass # 블록체인이라는 클래스를 만들고 그걸 프리셋으로? 만든다
'''
블록체인 초기화
제네시스 블록 생성
가장 최근에 추가한 블록을 가져온다
새로운 블록을 추가한다
블록체인의 유효성을 검증한다
블록체인의 데이터를 출력한다
'''
          
if __name__ == "__main__":
    my_blockchain = Blockchain()
    
    my_blockchain.add_block("A가 B에게 10 코인 전송")
    my_blockchain.add_block("B C에게 5 코인 전송")
    my_blockchain.add_block("C가 A에게 3 코인 전송")
    
    my_blockchain.display_chain()
    
    print(f"\n블록체인 유효성: {my_blockchain.is_chain_valid()}")

'''
<<<블록체인을 시뮬레이션하는 코드>>>
거래 내역을 담은 블록을 추가한다. 3개정도?
모든 블록의 상태 정보를 화면에 표시한다
유효성 검증 결과를 표시한다


<<<해킹 시뮬레이션>>>
블록 1번의 데이터를 10코인에서 1000코인으로 변조한 상황을 가정한다
유효성 검증을 한다
해시값을 비교해서 맞지 않다면 검증 실패 메세지를 출력한다

'''
