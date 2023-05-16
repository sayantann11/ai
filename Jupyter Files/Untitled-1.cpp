/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
int sum(struct TreeNode* A)
{
    if(A==NULL)
    {
        return 0;
    }
    return sum(A->left)+A->val+sum(A->right);
}

int Solution::solve(TreeNode* A) {
    int ls, rs;
 
    // If node is NULL or it's a leaf
    // node then return true
    if (A== NULL ||
       (A->left == NULL &&
        A->right == NULL))
        return 1;
    ls = sum(A->left);
    rs = sum(A->right);
    if((A->val==ls+rs)&&solve(A->left)&&solve(A->right));
    {
        return 1;
    }
    return 0;
    
}
