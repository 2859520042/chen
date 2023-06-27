#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <algorithm>
#include <chrono>
#include <thread>
using namespace std;
struct Expression {
    vector<int> numbers;
    vector<char> operators;
    int value;
    int operations;

    bool operator<(const Expression& other) const {
        return operations > other.operations;
    }
};
void evaluate(Expression& expr) {
    int x = expr.numbers[0];
    for (int i = 0; i < expr.operators.size(); i++) {
        int num = expr.numbers[i + 1];
        char op = expr.operators[i];
        if (op == '+')
            x += num;
        else if (op == '-')
            x -= num;
        else if (op == '*')
            x *= num;
        else if (op == '/' && num != 0)
            x /= num;
    }
    expr.value = x;
}
void findExpression(const vector<int>& numbers, int target, ofstream& outputFile) {
    int n = numbers.size();
    priority_queue<Expression> pq;
    for (int i = 0; i < n; i++) {
        pq.push({{numbers[i]}, {}, numbers[i], 0});
    }
    int MAX_OPERATIONS = 49;
    while (!pq.empty()) {
        Expression curr_expr = pq.top();
        pq.pop();
        if (curr_expr.value == target) {
            outputFile << curr_expr.operations << endl;
            cout<<"运算次数为："<<curr_expr.operations << endl<<"表达式为：";
            for (int i = 0; i < curr_expr.numbers.size(); i++) {
                outputFile << curr_expr.numbers[i];
                cout<<curr_expr.numbers[i];
                if (i < curr_expr.operators.size()) {
                    outputFile << curr_expr.operators[i];
                    cout<<curr_expr.operators[i];
                }
                else{break;}
            }
            cout<<endl;
            outputFile << endl;
            return;
        }

        if (curr_expr.operations >= MAX_OPERATIONS) {
            break;
        }
        if(curr_expr.numbers.size()<n)
        for (char op : {'+', '-', '*', '/'}) {
            for (int i = 0; i < n; i++) {
            Expression new_expr = curr_expr;
            new_expr.operators.push_back(op);
            new_expr.operations += 1;
            if (find(new_expr.numbers.begin(), new_expr.numbers.end(), numbers[i]) == new_expr.numbers.end()) {
                new_expr.numbers.push_back(numbers[i]);
                evaluate(new_expr);
                if(new_expr.operators.size() == new_expr.numbers.size()-1)
                pq.push(new_expr);
                }
            }
        }
    }
    cout<<"No Solution!" << endl;
    outputFile << "No Solution!" << endl;
}

int main() {
    ifstream inputFile("input.txt");
    ofstream outputFile("output.txt");
    if (!inputFile) {
        cerr << "Failed to open input file." << endl;
        return 1;
    }
    int n, m;
    if (!(inputFile >> n >> m)) {
        cerr << "Failed to read input data." << endl;
        return 1;
    }
    cout<<"n:"<<n<<endl<<"m:"<<m<<endl;
    vector<int> numbers(n);
    for (int i = 0; i < n; i++) {
        if (!(inputFile >> numbers[i])) {
            cerr << "Failed to read input data." << endl;
            return 1;
        }
        cout<<"numbers "<<numbers[i]<<endl;
    }
    findExpression(numbers, m, outputFile);
    inputFile.close();
    outputFile.close();
    return 0;
}
