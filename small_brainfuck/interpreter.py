class Brainfuck:
    commands = ("+", "-", "<", ">", ".", ",", "[", "]")

    def __init__(self, raw_code):
        self.raw_code = raw_code
        self.code = self.cleanup()

    def cleanup(self):
        return list(filter(lambda t: t in Brainfuck.commands, self.raw_code))

    def execute(self):
        pointer = [0] * 30000
        pointer_location = 0
        exec_location = 0
        brace_matches = self.brace_match()

        while exec_location < len(self.code):
            if self.code[exec_location] == ">":
                pointer_location += 1
            elif self.code[exec_location] == "<":
                pointer_location -= 1
            elif self.code[exec_location] == "+":
                pointer[pointer_location] = (pointer[pointer_location] + 1) % 256
            elif self.code[exec_location] == "-":
                pointer[pointer_location] = (pointer[pointer_location] - 1) % 256
            elif self.code[exec_location] == ".":
                print(chr(pointer[pointer_location]), end="")
            elif self.code[exec_location] == ",":
                # TODO: implement input
                pass
            elif self.code[exec_location] == "[" and pointer[pointer_location] == 0:
                exec_location = brace_matches[exec_location]
            elif self.code[exec_location] == "]" and pointer[pointer_location] != 0:
                exec_location = brace_matches[exec_location]

            exec_location += 1

    def brace_match(self):
        """
        this function return a dictionary containing each opening brace
        and its closing brace
        """

        temp_stack = []
        brace_match = {}
        for i in range(len(self.code)):
            if self.code[i] == "[":
                temp_stack.append(i)
            elif self.code[i] == "]":
                brace_match[temp_stack[-1]] = i
                brace_match[i] = temp_stack.pop()

        temp_stack.clear()

        return brace_match
