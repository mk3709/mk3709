#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> PII;

struct Edge : PII {
    Edge(int a = 0, int b = 0, int i = 0, int l = 0){
        first = a; second = b; k = i; len = l;
    }
    int k, len;
} edge[500010];

struct Node {
    Node *fa, *ch[2];
    int sum, arc[2];
    bool rev;
    
    void init(){
        fa = ch[0] = ch[1] = 0;
        rev = false;
    }
    
    int get_sum() const {
        return this ? sum : 0;
    }
    int get_arc(int c) const {
        return ch[c] ? edge[arc[c]].len : 0;
    }
    
    void mark_rev(){
        if(this == 0) return;
        rev = !rev;
        swap(ch[0], ch[1]);
        swap(arc[0], arc[1]);
    }
    
    void push_down(){
        if(rev){
            rev = false;
            ch[0]->mark_rev();
            ch[1]->mark_rev();
        }
    }
    void update(){
        sum = ch[0]->get_sum() + get_arc(0)
            + ch[1]->get_sum() + get_arc(1);
    }

    void rotate(int c){
        Node *y = fa;
        y->ch[1 - c] = ch[c];
        if(ch[c])
            ch[c]->fa = y;
        fa = y->fa;
        if(y->fa != 0){
            if(y->fa->ch[0] == y)
                y->fa->ch[0] = this;
            else
                y->fa->ch[1] = this;
        }
        ch[c] = y;
        y->fa = this;
        y->update();
    }
    
    void splay(Node *f){
        push_down();
        while(fa != f){
            if(fa->fa == f){
                fa->push_down(); push_down();
                if(fa->ch[0] == this)
                    rotate(1);
                else
                    rotate(0);
            } else{
                Node *y = fa, *z = y->fa;
                z->push_down(); y->push_down(); push_down();
                if(z->ch[0] == y){
                    if(y->ch[0] == this)
                        y->rotate(1), rotate(1);
                    else
                        rotate(0), rotate(1);
                } else{
                    if(y->ch[1] == this)
                        y->rotate(0), rotate(0);
                    else
                        rotate(1), rotate(0);
                }
            }
        }
        update();
    }
} nodes[1000010], *ptr = nodes;

struct Administrator {
    int degree[100010];
    Node* mem[100010];

    Node* node(int v){
        return mem[v] ? mem[v] : (mem[v] = ptr++);
    }

    bool link(int v, int u, int p){
        node(v)->splay(0); node(u)->splay(0);
        if(node(v)->fa == 0 && node(u)->fa == 0){
            if(node(v)->ch[1]){
                node(v)->mark_rev();
                node(v)->push_down();
            }
            if(node(u)->ch[0]){
                node(u)->mark_rev();
                node(u)->push_down();
            }
            node(v)->ch[1] = node(u);
            node(v)->arc[1] = p;
            node(u)->fa = node(v);
            node(u)->arc[0] = p;
            node(v)->update();
            ++degree[v], ++degree[u];
            return true;
        } else{
            return false;
        }
    }
    
    void cut(int v, int u){
        node(v)->splay(0); node(u)->splay(node(v));
        if(node(v)->ch[0] == node(u)){
            node(v)->ch[0] = 0;
        } else{
            node(v)->ch[1] = 0;
        }
        node(v)->update();
        node(u)->fa = 0;
        --degree[v]; --degree[u];
    }
    
    int query(int v, int u){
        node(u)->splay(0); node(v)->splay(0);
        if(node(v)->fa == 0 && node(u)->fa == 0)
            return -1;
        node(u)->splay(node(v));
        if(node(v)->ch[0] == node(u))
            return node(v)->get_arc(0) + node(u)->ch[1]->get_sum()
                + node(u)->get_arc(1);
        else
            return node(u)->get_arc(0) + node(u)->ch[0]->get_sum()
                + node(v)->get_arc(1);
    }
    
    void modify(int v, int u){
        node(v)->splay(0); node(u)->splay(0);
    }
} admin[101];

int main(){
    int S, L, A, T;
    scanf("%d%d%d%d", &S, &L, &A, &T);
    for(int i = 0; i < L; ++i){
        int a, b, k;
        scanf("%d%d%d", &a, &b, &k);
        if(a > b) swap(a, b);
        edge[i] = Edge(a, b, k);
    }
    sort(edge, edge + L);
    for(int i = 0; i < L; ++i)
        admin[edge[i].k].link(edge[i].first, edge[i].second, i);
    for(int i = 0; i < T; ++i){
        int opt; scanf("%d", &opt);
        if(opt == 1){
            int a, b, k;
            scanf("%d%d%d", &a, &b, &k);
            if(a > b) swap(a, b);
            int p = lower_bound(edge, edge + L, PII(a, b)) - edge;
            if(p == L || edge[p] != PII(a, b)){
                puts("Wrong link");
            } else if(edge[p].k == k){
                puts("Already controlled link");
            } else if(admin[k].degree[a] == 2 || admin[k].degree[b] == 2){
                puts("Server overload");
            } else if(!admin[k].link(a, b, p)){
                puts("Network redundancy");
            } else{
                admin[edge[p].k].cut(a, b);
                edge[p].k = k;
                puts("Assignment done");
            }
        } else if(opt == 2){
            int a, b, x;
            scanf("%d%d%d", &a, &b, &x);
            if(a > b) swap(a, b);
            int p = lower_bound(edge, edge + L, PII(a, b)) - edge;
            edge[p].len = x;
            admin[edge[p].k].modify(a, b);
        } else{
            int a, b, k;
            scanf("%d%d%d", &a, &b, &k);
            int r = admin[k].query(a, b);
            if(r == -1){
                puts("No connection");
            } else{
                printf("%d security devices placed\n", r);
            }
        }
    }
    return 0;
}
