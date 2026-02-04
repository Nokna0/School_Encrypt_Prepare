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
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 3
    
    def create_genesis_block(self):
        return Block(0, "0", time.time(), "제네시스 블록")
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_block = Block(
            index=previous_block.index + 1,
            previous_hash=previous_block.hash,
            timestamp=time.time(),
            data=data
        )
        
        print(f"\n블록 #{new_block.index} 채굴 중...")
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        
    def is_chain_valid(self):
        # 블록체인 무결성 검증
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            if current_block.hash != current_block.calculate_hash():
                print(f"블록 #{i}의 해시가 유효하지 않습니다!")
                return False
            
            if current_block.previous_hash != previous_block.hash:
                print(f"블록 #{i}의 체인 연결이 끊어졌습니다!")
                return False
        return True
    
    def display_chain(self):
        print("\n===== 블록체인 =====")
        for block in self.chain:
            print(f"\n블록 #{block.index}")
            print(f"    타임스탬프: {time.ctime(block.timestamp)}")
            print(f"    데이터: {block.data}")
            print(f"    이전 해시: {block.previous_hash}")
            print(f"    현재 해시: {block.hash}")
            print(f"Nonce: {block.nonce}")
'''
블록체인 초기화 완
제네시스 블록 생성 완
가장 최근에 추가한 블록을 가져온다 완
새로운 블록을 추가한다 완
블록체인의 유효성을 검증한다 완
블록체인의 데이터를 출력한다 완
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
거래 내역을 담은 블록을 추가한다. 3개정도? 완
모든 블록의 상태 정보를 화면에 표시한다 완
유효성 검증 결과를 표시한다 완


<<<해킹 시뮬레이션>>>
블록 1번의 데이터를 10코인에서 1000코인으로 변조한 상황을 가정한다
유효성 검증을 한다
해시값을 비교해서 맞지 않다면 검증 실패 메세지를 출력한다

'''
