class Brainfuck:
    commands = ("+", "-", "<", ">", ".", ",", "[", "]")

    def __init__(self, raw_code):
        self.raw_code = raw_code
        self.code = self.cleanup(raw_code)

    def cleanup(self, raw_code):
        return list(filter(lambda t: t in Brainfuck.commands, raw_code))

    def execute(self, code):
        pointer = [0] * 30000
        pointer_location = 0
        exec_location = 0
        brace_matches = self.brace_match(code)

        while exec_location < len(code):
            if code[exec_location] == ">":
                pointer_location += 1
            elif code[exec_location] == "<":
                pointer_location -= 1
            elif code[exec_location] == "+":
                pointer[pointer_location] = (pointer[pointer_location] + 1) % 256
            elif code[exec_location] == "-":
                pointer[pointer_location] = (pointer[pointer_location] - 1) % 256
            elif code[exec_location] == ".":
                print(pointer[pointer_location])
            elif code[exec_location] == ",":
                # pointer[loc] = ord(program_input.pop(0))
                pass
            elif code[pointer_location] == "[" and code[pointer_location] == 0:
                exec_location = brace_matches[exec_location]
            elif code[pointer_location] == "]" and code[pointer_location] != 0:
                exec_location = brace_matches[exec_location]

            exec_location += 1
            #print(exec_location)

    def brace_match(self, code):
        """
        this function return a dictionary containing each opening brace
        and its closing brace
        """

        temp_stack = []
        brace_match = {}
        for i in range(len(code)):
            if self.code[i] == "[":
                temp_stack.append(i)
            elif self.code[i] == "]":
                brace_match[temp_stack[-1]] = i
                brace_match[i] = temp_stack.pop()

        temp_stack.clear()

        return brace_match
