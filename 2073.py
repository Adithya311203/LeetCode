def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        m=0
        i=0
        key=tickets[k]
        while(tickets[k]>0):
            if i==len(tickets):
                i=0
            if tickets[i]>0:
                m+=1
                tickets[i]-=1
            i+=1
        return m