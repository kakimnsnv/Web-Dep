class Node {
    constructor(data) {
      this.data = data;
      this.left = null;
      this.right = null;
    }
}
  
class BST {
    constructor() {
      this.root = null;
    }
  
    insert(data) {
      const newNode = new Node(data);
      if (this.root === null) {
        this.root = newNode;
      } else {
        this.insertNode(this.root, newNode);
      }
    }
  
    insertNode(node, newNode) {
      if (newNode.data < node.data) {
        if (node.left === null) {
          node.left = newNode;
        } else {
          this.insertNode(node.left, newNode);
        }
      } else {
        if (node.right === null) {
          node.right = newNode;
        } else {
          this.insertNode(node.right, newNode);
        }
      }
    }

    getHeight(node) {
      if (node === null) return 0;
      return Math.max(this.getHeight(node.left), this.getHeight(node.right)) + 1;
    }

    getNodesByLevel() {
      const levels = [];
      this.getNodesByLevelHelper(this.root, 0, levels);
      return levels;
    }
    
    getNodesByLevelHelper(node, level, levels) {
      if (node === null) return;
    
      if (levels[level] === undefined) {
        levels[level] = [];
      }
    
      levels[level].push(node.data);
    
      this.getNodesByLevelHelper(node.left, level + 1, levels);
      this.getNodesByLevelHelper(node.right, level + 1, levels);
    }
  
  async generateTree() {
      const height = this.getHeight(this.root);
      const width = Math.pow(2, height) - 1;
      const table = document.getElementById('bst');
      table.innerHTML = '';
      // this.addNodes(table, this.root, 0, width / 2, width);
     var levels = this.getNodesByLevel();
     levels.map((level, index) => {
      const row = table.insertRow(index);
      level.map(async (node, i) => {
        for(let k = 0; k < width; k++){
          await row.insertCell(i);
        }
        row.cells.map((cell, i) => {
          if(i < width/ level.length){
            cell.classList.add('spacer');
          }else{
            cell.textContent = node.data;
          }
        })
        for(let k = 0; k < width / level.length; k++){
          await row.insertCell(i).classList.add('spacer');
        }
        const cell = await row.insertCell(i);
        cell.textContent = node;
        for(let k = 0; k < width / level.length; k++){
          await row.insertCell(i).classList.add('spacer');
        }
      });
     });
    }
    
    addNodes(table, node, level, position, previousPos) {
        if (node !== null) {
          if (table.rows[level] === undefined) {
            const row = table.insertRow(level);
            for (let i = 0; i < Math.pow(2, level); i++) {
              row.insertCell(-1).classList.add('spacer');
            }
          }
    
          const existingCells = table.rows[level].cells.length;
          const middle = Math.floor(existingCells / 2);
          let cellPosition = middle + position;
          cellPosition = Math.max(-1, Math.min(existingCells, cellPosition)); // Ensure position within range
          
          if (level > 0) {
            const cell = table.rows[level].insertCell(cellPosition);
            cell.textContent = node.data;
          } else {
            const cell = table.rows[level].insertCell(cellPosition);
            cell.textContent = node.data;
            cell.colSpan = Math.pow(2, level + 1) - 1;
          }
    
          this.addNodes(table, node.left, level + 1, position / 2, position);
          this.addNodes(table, node.right, level + 1, position * 2,position);
        } else if (level < table.rows.length) {
          const cell = table.rows[level].insertCell(position);
          cell.classList.add('empty');
        }
    }
    
    
    
    
}
  
  const bst = new BST();
  bst.insert(10);
  bst.insert(5);
  bst.insert(15);
  bst.insert(3);
  bst.insert(7);
  bst.insert(12);
  bst.insert(20);
//   bst.insert(21);
//   bst.insert(19);
// document.getElementById('btn').addEventListener('click', () => {
  bst.generateTree();
// });