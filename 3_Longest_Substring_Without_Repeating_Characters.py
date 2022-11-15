

class Solution:


    def verificarTamanho(self, start, end, string, maior) -> int:
        if len(string[start:end+1]) > maior:
            return len(string[start:end+1])
        else:
            return maior


    def lengthOfLongestSubstring(self, s: str) -> int:
        maior = -1

        tamanho = len(s)
        tam = tamanho

        i, j = -1, -1
        sub = ""

        for h in range(tamanho):
            for k in range(tam):

                if s[k] in sub:
                    maior = self.verificarTamanho(i, j, s, maior)
                    sub = ""
                    tam = k
                    break


                i = h
                j = k
                sub = sub + s[k]

        
        return maior

        #print(sub)

# https://leetcode.com/problems/longest-substring-without-repeating-characters/


if __name__ == "__main__":
    s = Solution()
    s.lengthOfLongestSubstring("abcabcbb")