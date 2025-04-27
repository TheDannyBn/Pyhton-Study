board = {
    '1h': 'bking',
    '6c': 'wqueen',
    '2g': 'bbishop',
    '5h': 'bqueen',
    '3e': 'wking'
}

def isValidChessBoard(board):
    valid_pieces = {'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'}
    valid_rows = '12345678'
    valid_columns = 'abcdefgh'
    
    piece_count = {'w': 0, 'b': 0}
    pawn_count = {'w': 0, 'b': 0}
    king_count = {'w': 0, 'b': 0}
    
    for position, piece in board.items():
        # בדיקת מיקום חוקי
        if len(position) != 2 or position[0] not in valid_rows or position[1] not in valid_columns:
            return False
        
        # בדיקת שם כלי חוקי
        if len(piece) < 2 or piece[0] not in ('w', 'b') or piece[1:] not in valid_pieces:
            return False
        
        color = piece[0]
        piece_type = piece[1:]
        
        piece_count[color] += 1
        
        if piece_type == 'pawn':
            pawn_count[color] += 1
        if piece_type == 'king':
            king_count[color] += 1
    
    # בדיקה סופית
    if king_count['w'] != 1 or king_count['b'] != 1:
        return False
    if piece_count['w'] > 16 or piece_count['b'] > 16:
        return False
    if pawn_count['w'] > 8 or pawn_count['b'] > 8:
        return False
    
    return True
