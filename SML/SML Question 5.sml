datatype 'a BinaryTree = btempty | bt of 'a * 'a BinaryTree * 'a BinaryTree ;

fun lookup (btempty,_) = false
|   lookup(bt(root:int,left,right),x:int) =
    if (x = root) then true
    else (if (x <= root) then lookup(left,x)
          else lookup(right,x) );

val Tree = bt(2,btempty,
 bt(3,btempty,
 bt(7,bt(6,bt(5,btempty,btempty),
 btempty), 
 bt(8,btempty,btempty)) ));

val Tree2 = bt (2,btempty,bt (3,btempty,btempty));

lookup(Tree,6);
lookup(Tree2,6);
lookup(Tree,1);
lookup(Tree2,1);

fun inorder (btempty) = []
| inorder(bt(root:'a,left,right)) = inorder(left) @ (root :: inorder(right));
    
fun preorder (btempty) = []
| preorder(bt(root:'a,left,right)) = root :: (preorder(left) @ preorder(right));

fun postorder (btempty) = []
| postorder(bt(root:'a,left,right)) =(postorder(left) @ postorder(right)) @ (root :: []);

inorder(Tree);
inorder(Tree2);
preorder(Tree);
preorder(Tree2);
postorder(Tree);
postorder(Tree2);

fun left_subtree btempty = btempty
| left_subtree(bt(_,left,_ )) = left;

fun right_subtree btempty = btempty
| right_subtree(bt(_ ,_ ,right)) = right;


exception label_has_nil_argument;

fun label btempty = raise label_has_nil_argument
| label(bt(value,_ ,_ )) = value;


left_subtree(Tree);
left_subtree(Tree2);
right_subtree(Tree);
right_subtree(Tree2);
label(Tree);
label(Tree2);