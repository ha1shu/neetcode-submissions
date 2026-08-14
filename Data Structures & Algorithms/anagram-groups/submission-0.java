class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> map = new HashMap<>();
        for(String str: strs){

            char[] strArray = str.toCharArray();

            Arrays.sort(strArray);
            String newString = new String(strArray);

            if(!map.containsKey(newString)){
                map.put(newString, new ArrayList<String>());
            }
                
            map.get(newString).add(str);
        }

        return new ArrayList<>(map.values());
    }
}