from collections import deque

class NFA:
    def __init__(self,states,alphabet,delta,start,finals):
        self.states = states
        self.alphabet = alphabet
        self.delta = delta
        self.start = start
        self.finals = finals

    def get_transition(self,state,symbol):
        if (state,symbol) in self.delta:
            return self.delta[(state,symbol)]
        else:
            return set()
            
    def get_lambda_closure(self,states):
        closure = set(states)
        queue = deque(states)
        while queue:
            curr = queue.popleft()
            for next_state in self.get_transition(curr,''):
                if next_state not in closure:
                    closure.add(next_state)
                    queue.append(next_state)
        return frozenset(closure)
        
    def is_final(self,state):
        return state in self.finals
        
def tabdil(nfa):
        queue = deque()
        start = nfa.get_lambda_closure([nfa.start])
        
        queue.append(start)
        dfa_states = set([start])
        dfa_transitions = {}
        dfa_finals = set()
        alphabet = nfa.alphabet
                  
        while queue:
            curr = queue.popleft()
            for symbol in alphabet:
                next_states = set()
                for state in curr:
                    next_states |= nfa.get_transition(state, symbol)
                next_states = nfa.get_lambda_closure(next_states)
                next_states = frozenset(next_states)
                if next_states not in dfa_states:
                    dfa_states.add(next_states)
                    queue.append(next_states)
                dfa_transitions[(curr, symbol)] = next_states

        for state in dfa_states:
            if any(nfa.is_final(s) for s in state):
                dfa_finals.add(state)
        return dfa_transitions


nfa_states = set(['q0', 'q1', "q2"])
nfa_alphabet = set(['a', 'b'])
nfa_delta = {
             ('q0', 'b'): {'q1'},
             ("q0", "") : {"q1"},
             ("q0", "") : {"q2"},
             ("q1", "a") : {"q2"}

}
nfa_start = 'q0'
nfa_finals = set(['q1'])

nfa = NFA(nfa_states, nfa_alphabet, nfa_delta, nfa_start, nfa_finals)
dfa = tabdil(nfa)
print(dfa)