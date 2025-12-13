def validateCoupons(code, businessLine, isActive):
        result = []
        businessOrder = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }

        n = len(code)

        for i in range(n):

            if isActive[i] == False:
                continue

            if businessLine[i] not in businessOrder:
                continue

            if len(code[i]) == 0:
                continue

            validCode = True
            for ch in code[i]:
                if not (ch.isalnum() or ch == "_"):
                    validCode = False
                    break

            if validCode == False:
                continue

            result.append([businessOrder[businessLine[i]], code[i]])

        result.sort()

        answer = []
        for item in result:
            answer.append(item[1])

        return answer