class OrderedStream {
    int ptr, n;
    String[] stream;
    public OrderedStream(int n) {
        ptr = 0;
        this.n = n;
        stream = new String[n];
    }
    
    public List<String> insert(int idKey, String value) {
        idKey -= 1;
        stream[idKey] = value;
        List<String> ans = new ArrayList<>();
        if(idKey != ptr) return ans;
        while(ptr < n && stream[ptr] != null) {
            ans.add(stream[ptr++]);
        }
        return ans;
    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * OrderedStream obj = new OrderedStream(n);
 * List<String> param_1 = obj.insert(idKey,value);
 */