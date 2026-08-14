class Solution {
    public int characterReplacement(String s, int k) {
        int n = s.length();
        int maxLen = 0;
        for(int i = 0 ; i<n ; i++){
            int freq[] = new int[26];
            int maxFreq = 0;

            for(int j = i ; j<n;j++){
                freq[s.charAt(j)-'A']++;
                maxFreq = Math.max(maxFreq,freq[s.charAt(j)-'A']);

                int length = j-i+1;
                int change = length - maxFreq;

                if(change<=k){
                    maxLen=Math.max(maxLen,length);
                }
            }
        }
        return maxLen;
    }
}
